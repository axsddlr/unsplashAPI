import requests


class unslph:

    @staticmethod
    def unsplash(search, page_number):
        url = f"https://unsplash.com/napi/search?query={search}&per_page=20&page={page_number}&order_by" \
              f"=relevance&xp "

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 "
                          "Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status = response.status_code

        api_response = response.json()

        api = []
        for each in api_response["photos"]["results"]:
            img_full = each["urls"]["full"]
            post_id = each["id"]
            color = each["color"]
            description = each["description"]

            api.append(
                {
                    "id": post_id,
                    "img": img_full,
                    "color": color,
                    "description": description
                }
            )

        if status != 200:
            raise Exception("API response: {}".format(status))
        return api

    @staticmethod
    def unsplash_search(search):
        final_list = []
        for x in range(1, 11):
            final_list.extend(unslph.unsplash(search, x))
        return final_list

    @staticmethod
    def unsplash_topics_parse(topics, page_number):
        url = f"https://unsplash.com/napi/topics/{topics}/photos?page={page_number}&per_page=20"

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 "
                          "Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status = response.status_code

        api_response = response.json()

        api = []
        for each in api_response:
            img_full = each["urls"]["full"]
            post_id = each["id"]
            color = each["color"]
            description = each["description"]

            api.append(
                {
                    "id": post_id,
                    "img": img_full,
                    "color": color,
                    "description": description
                }
            )

        if status != 200:
            raise Exception("API response: {}".format(status))
        return api

    @staticmethod
    def unsplash_topics(topics):
        final_list = []
        for x in range(1, 20):
            final_list.extend(unslph.unsplash_topics_parse(topics, x))
        return final_list

    @staticmethod
    def unsplash_main_parse(page_number):
        url = f"https://unsplash.com/napi/photos?per_page=24&page={page_number}"

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 "
                          "Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status = response.status_code

        api_response = response.json()

        api = []
        for each in api_response:
            img_full = each["urls"]["full"]
            post_id = each["id"]
            color = each["color"]
            description = each["description"]

            api.append(
                {
                    "id": post_id,
                    "img": img_full,
                    "color": color,
                    "description": description
                }
            )

        if status != 200:
            raise Exception("API response: {}".format(status))
        return api

    @staticmethod
    def unsplash_main():
        final_list = []
        for x in range(1, 20):
            final_list.extend(unslph.unsplash_main_parse(x))
        return final_list
