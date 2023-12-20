import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def process_data():
    data = pd.read_csv(
        "https://stats.moe.gov.tw/files/detail/111/111_student.csv", encoding="utf-8"
    )
    data.isnull().sum().sum()
    school_SorI = []

    for i in data["學校名稱"]:
        if ("國立" in i) or ("市立" in i):
            school_SorI.append("國立")
        else:
            school_SorI.append("私立")
    data["公私立"] = school_SorI

    return data


def deal_data(data):
    data_buf = data.drop_duplicates(subset=["學校名稱"])
    school_name = data_buf["學校名稱"].unique()
    school_count = data_buf["公私立"].value_counts()
    school_SorI = data_buf["公私立"].unique()
    school_num = school_name.__len__()

    city_list = []
    for i in data["縣市名稱"]:
        city_list.append(i[3:])
    data["縣市名稱"] = city_list

    city_to_area = {
        "臺北市": "北部",
        "新北市": "北部",
        "基隆市": "北部",
        "新竹市": "北部",
        "桃園市": "北部",
        "新竹縣": "北部",
        "宜蘭縣": "北部",
        "臺中市": "中部",
        "苗栗縣": "中部",
        "彰化縣": "中部",
        "南投縣": "中部",
        "雲林縣": "中部",
        "高雄市": "南部",
        "臺南市": "南部",
        "嘉義市": "南部",
        "嘉義縣": "南部",
        "屏東縣": "南部",
        "澎湖縣": "南部",
        "花蓮縣": "東部",
        "臺東縣": "東部",
        "金門縣": "福建省",
    }

    data["區域"] = data["縣市名稱"].map(city_to_area)

    data_buf = data.drop_duplicates(subset=["縣市名稱", "學校名稱", "區域"])
    school_city = data_buf["縣市名稱"].value_counts()

    city_list = data_buf["縣市名稱"].unique()

    data_buf = data.drop_duplicates(subset=["學校名稱", "等級別"])
    grade_count = data_buf["等級別"].value_counts()
    grade_name = data_buf["等級別"].unique()
    return school_count, school_num, school_city, grade_count, grade_name


@app.route("/")
def form():
    data = process_data()
    (
        school_count,
        school_num,
        school_city,
        grade_count,
        grade_name,
    ) = deal_data(data)
    result = school_count.to_json(orient="records")
    print(school_count)
    return render_template("index.html", exchangedata=school_count)


if __name__ == "__main__":
    a = app.run()
