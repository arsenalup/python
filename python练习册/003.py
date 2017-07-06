import uuid
import redis


def create_code(num, length):
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
        if len(result) == num:
            break
    return result


def save_to_redis(num_list):
    r = redis.Redis(host='', port='', db='')
    for code in num_list:
        r.lpush('code', code)


save_to_redis(create_code(200, 20))