import sys
import configparser

# Azure Text Analytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import azure.ai.vision as sdk

from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot import LineBotApi, WebhookHandler

# Config Parser
config = configparser.ConfigParser()
config.read("config.ini")

# Config Azure Analytics
credential = AzureKeyCredential(config["AzureLanguage"]["API_KEY"])
service_options = sdk.VisionServiceOptions(
    config["AzureVision"]["VISION_ENDPOINT"], config["AzureVision"]["VISION_KEY"]
)

app = Flask(__name__)

channel_access_token = config["Line"]["CHANNEL_ACCESS_TOKEN"]
channel_secret = config["Line"]["CHANNEL_SECRET"]
line_bot_api = LineBotApi("apikey")
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

handler = WebhookHandler(channel_secret)

configuration = Configuration(access_token=channel_access_token)


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print(body)

    # parse webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    translate = {"positive": "正向", "negative": "正向", "neutral": "中性"}
    sentiment_result = azure_sentiment(event.message.text)
    analysis_result = sentiment_result[0]
    result = sentiment_result[1][analysis_result]
    result = (
        translate[analysis_result] + "。分數:" + str(result) + str(sentiment_result[2])
    )
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=result)],
            )
        )


def image_process(message):
    image_url = line_bot_api.get_message_content(message_id).content_url
    vision_source = sdk.VisionSource(
        url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
    )


if __name__ == "__main__":
    app.run()
