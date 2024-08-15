from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger  # flasgger make API docs

import book_review

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

br = book_review.BookReview()


class AllReviews(Resource):
    def get(self):
        """
        This method responds to the GET request for retrieving all book reviews.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: sort
              in: query
              type: string
              required: false
              enum: [asc, desc]
              description: The sort order for the reviews (ascending or descending)
            - name: max_records
              in: query
              type: integer
              required: false
              description: The maximum number of records to return
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: array
                        items:
                          type: object
                          properties:
                            book_title:
                              type: string
                              description: The book title
                            book_rating:
                              type: number
                              description: The book rating
                            book_notes:
                              type: string
                              description: Additional notes
        """

        sort = request.args.get("sort", default=None)
        max_records = int(request.args.get("max_records", default=10))

        # Validate the sort parameter
        if sort and sort not in ["ASC", "DESC"]:
            return {"error": "Invalid sort parameter"}, 400

        # Sort the reviews based on the sort parameter
        if sort == "ASC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        elif sort == "DESC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        else:
            book_reviews = br.get_book_ratings(max_records=max_records)

        return book_reviews, 200


class UppercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get("text")

        return {"text": text.upper()}, 200


class ProcessText(Resource):
    def get(self):
        """
        This method responds to the GET request for processing text and returns the processed text.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be processed
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: The number of times to duplicate the text
            - name: capitalization
              in: query
              type: string
              required: false
              enum: [UPPER, LOWER, None]
              description: The capitalization to apply to the text
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            processed_text:
                                type: string
                                description: The processed text
        """
        text = request.args.get("text")
        duplication_factor = request.args.get("duplication_factor", 1)
        capitalization = request.args.get("capitalization", "None")

        # Convert duplication_factor to an integer
        try:
            duplication_factor = int(duplication_factor)
        except ValueError:
            return {"error": "Invalid duplication factor value"}, 400

        # Validate capitalization input
        if capitalization not in ["UPPER", "LOWER", "None"]:
            return {"error": "Invalid capitalization value"}, 400

        # Process text based on capitalization and duplication factor
        if capitalization == "UPPER":
            text = text.upper()
        elif capitalization == "LOWER":
            text = text.lower()

        processed_text = text * duplication_factor

        return {"processed_text": processed_text}, 200


api.add_resource(AllReviews, "/all_reviews")
api.add_resource(ProcessText, "/process_text")
api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)
