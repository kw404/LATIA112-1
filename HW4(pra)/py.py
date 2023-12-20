import pandas as pds
import matplotlib.pyplot as plt
import random

plt.rc("font", family="Microsoft JhengHei")  # 讓 plt 可以顯示中文

data = pds.read_csv("111_students.csv", encoding="utf-8")
data.isnull().sum().sum()  # 檢查空值數量


def create_count_dict(data, count):  # 建立多層 dict 結構來儲存各校在學與延修生的男女生數
    data_buf = data.drop_duplicates("學校代碼")
    for i in data_buf["學校名稱"]:
        count[i] = {}
        count[i]["在學生"] = {}
        count[i]["在學生"]["男生數"] = 0
        count[i]["在學生"]["女生數"] = 0


def count_every_schools_data(data):
    for j in range(len(data)):
        count[data.iloc[j, 2]]["在學生"]["男生數"] += int(data.iloc[j, 8])
        count[data.iloc[j, 2]]["在學生"]["女生數"] += int(data.iloc[j, 9])


school_SorI = []

for i in data["學校名稱"]:
    if ("國立" in i) or ("市立" in i):
        school_SorI.append("國立")
    else:
        school_SorI.append("私立")

data["公私立"] = school_SorI  # 將 Dataframe 新增「公私立」column

data_buf = data.drop_duplicates(subset=["學校名稱"])

school_name = data_buf["學校名稱"].unique()
school_count = data_buf["公私立"].value_counts()
school_SorI = data_buf["公私立"].unique()
school_num = school_name.__len__()
print("目前有", school_num, "間大專院校")
print(f'其中國立學校有{school_count["國立"]}間,私立有{school_count["私立"]}間')
plt.pie(school_count, radius=1.5, labels=school_SorI)
plt.show()

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
# area_list.sort(area_list['區域'])
print(f"本資料集共收集了 {school_num} 所學校，其中：")

for city in city_list:
    print(f"{city} 有 {school_city[city]} 所大專院校")

plt.pie(school_city, radius=1.5, labels=city_list)
plt.show()

data_buf = data.drop_duplicates(subset=["學校名稱", "等級別"])
grade_count = data_buf["等級別"].value_counts()
grade_name = data_buf["等級別"].unique()

plt.pie(grade_count, radius=1.5, labels=grade_name)
plt.show()

data_buf = data.drop_duplicates(subset=["學校名稱", "體系別"])
grade_count = data_buf["體系別"].value_counts()
grade_name = data_buf["體系別"].unique()

plt.pie(grade_count, radius=1.5, labels=grade_name)
plt.show()

data_buf = data.drop_duplicates(subset=["縣市名稱", "學校名稱", "區域"])

school_area = data_buf["區域"].value_counts()
area_list = data_buf["區域"].unique()
for area in area_list:
    print(f"{area} 有 {school_area[area]} 所大專院校")

plt.pie(school_area, radius=1.5, labels=area_list)
plt.show()

girl_num = sum(data["女生計"])
boy_num = sum(data["男生計"])

student_sum = [girl_num, boy_num]
label_student = ["女生", "男生"]

print(f"全台有", girl_num, "位女學生")
print(f"全台有", boy_num, "位男學生")
print(f"學生總數為", boy_num + girl_num, "位")

plt.pie(student_sum, radius=1.5, labels=label_student)
plt.show()

count = {}

create_count_dict(data, count)
count_every_schools_data(data)
