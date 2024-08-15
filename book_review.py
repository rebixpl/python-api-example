import os
from pyairtable import Api

# api_key = os.environ.get("AIRTABLE_API_KEY")
# api = Api(api_key)
# table = api.table("appxvEY4zTWDC23OQ", "tblKZYE5iH80o5hgV")
# print(table.all())


class BookReview:
    def __init__(self):
        self.api = Api(os.environ.get("AIRTABLE_API_KEY"))
        self.table = self.api.table("appxvEY4zTWDC23OQ", "tblKZYE5iH80o5hgV")

    def get_book_ratings(self, sort="ASC", max_records=10):
        rating = ["Rating"]
        if sort == "DESC":
            rating = ["-Rating"]
        table = self.table.all(sort=rating, max_records=max_records)

        return table

    def add_book_rating(self, book_title, book_rating, notes=None):
        fields = {"Book": book_title, "Rating": book_rating, "Notes": notes}
        self.table.create(fields)


if __name__ == "__main__":
    br = BookReview()
    print(br.get_book_ratings(sort="DESC", max_records=10))
    # br.add_book_rating("Giga Book", 6.2, "Great book! Must read!")
