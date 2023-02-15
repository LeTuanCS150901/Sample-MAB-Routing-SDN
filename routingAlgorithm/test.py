import matplotlib.pyplot as plt
from MAB import GreedyBandit, UCBBandit, SoftmaxBandit
from Database.LinkCostDB import MongoDbHandler

# # Connect to the MongoDB database
# client = pymongo.MongoClient("mongodb://TuanNguyen:Tuan150901@ac-nazxr98-shard-00-00.cas1oue.mongodb.net:27017,ac-nazxr98-shard-00-01.cas1oue.mongodb.net:27017,ac-nazxr98-shard-00-02.cas1oue.mongodb.net:27017/?ssl=true&replicaSet=atlas-9xwzc3-shard-0&authSource=admin&retryWrites=true&w=majority")

# # Select the database you want to work with
# db = client["SDN_data"]

# # Select the collection you want to work with
# collection = db["Reward_data"]


# test data
test_data = {
    0: {'ip_server': "10.0.0.2", 'total_cost': 2},

    1: {'ip_server': "10.0.0.4", 'total_cost': 4}

}

# arms = so luong server
greedy_object = GreedyBandit.Greedy(arms=2, arms_data=test_data, epsilon=0.4)

# greedy_object = UCBBandit.UCB(
#     arms=2, arms_data=test_data, constant=2)

# greedy_object = SoftmaxBandit.Softmax(
#     arms=2, arms_data=test_data, temperature=2)


# create mongo DB instance
db = MongoDbHandler(database="SDN_data", collection="Reward_data")

# remove all old data
db.remove_all()

# global
total_rewards = 0
average_rewards_history = []
i = 0

count_1 = 0
count_2 = 0
for i in range(10):
    # chen vao doan chon server o file Dijsktra
    arm = greedy_object.choose_arm()
    reward = greedy_object.get_reward(arm)
    greedy_object.update(arm, reward)
    total_rewards += reward
    current_avg_reward = total_rewards / (i+1)
    average_rewards_history.append(current_avg_reward)
    # hien thi ip cua server
    print(test_data[arm])
    if arm == 0:
        count_1 += 1
    else:
        count_2 += 1

    # chen reward tich luy va server duoc chon vao db
    db.insert_one_data({
        "ip_server": test_data[arm]['ip_server'],
        "avg_reward": current_avg_reward
    })


print(count_1, count_2)
# return server
# print(test_data[arm])
# print(total_rewards)


# plt.plot(range(len(average_rewards_history)), average_rewards_history, label="greedy")
# plt.legend()
# plt.show()

# luu ip server duoc chon va reward tich luy o time do
