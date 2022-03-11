class Users(Resource):
    # Write method to fetch data from the CSV file
    def get(self):
        pass

    def post(self):
        # Write method to write data to the CSV file
        pass

    def delete(self):
        # Write method to update data in the CSV file
        pass


# Add URL endpoints
api.add_resource(Users, '/users')