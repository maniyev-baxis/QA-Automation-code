# import pytest

# USER_ENDPOINT = "/v2/user"


# @pytest.mark.tags("login")
# @pytest.mark.parametrize(
#     "username,password,expected_status",
#     [
#         ("emin.muhammadi", "mysecretpassword", 200),
#         ("john.doe", "pwd", 200),
#     ],
# )
# def test_users_should_be_able_to_login(
#     petstore_api, username, password, expected_status
# ):
#     response = petstore_api.get(
#         f"{USER_ENDPOINT}/login", params={"username": username, "password": password}
#     )
#     assert response.status == expected_status


# @pytest.mark.tags("logout")
# def test_users_should_be_able_to_logout(petstore_api):
#     response = petstore_api.get(f"{USER_ENDPOINT}/logout")
#     assert response.status == 200


# @pytest.mark.tags("create_user")
# @pytest.mark.parametrize(
#     "user_data, expected_status",
#     [
#         (
#             {
#                 "username": "emin.muhammadi",
#                 "firstName": "Emin",
#                 "lastName": "Muhammadi",
#                 "email": "emin.muhammadi@localhost",
#                 "password": "secretpassword",
#                 "phone": "+994911",
#             },
#             200,
#         ),
#     ],
# )
# def test_users_should_be_able_to_create_user(petstore_api, user_data, expected_status):
#     response = petstore_api.post(f"{USER_ENDPOINT}", data=user_data)
#     assert response.status == expected_status


# @pytest.mark.tags("update_user")
# @pytest.mark.parametrize(
#     "username, user_data, expected_status",
#     [
#         (
#             "emin.muhammadi",
#             {
#                 "firstName": "Emin",
#                 "lastName": "Muhammadi",
#                 "email": "emin.muhammadi@localhost",
#                 "password": "newsecretpassword",
#                 "phone": "+994911",
#             },
#             200,
#         ),
#     ],
# )
# def tests_users_should_be_able_to__put_metod(
#     petstore_api, username, user_data, expected_status
# ):
#     response = petstore_api.put(f"{USER_ENDPOINT}/{username}", data=user_data)
#     assert response.status == expected_status


# @pytest.mark.tags("delete_user")
# @pytest.mark.parametrize(
#     "username, expected_status",
#     [
#         ("emin.muhammadi", 200),
#     ],
# )
# def test_users_should_be_able_to_delete_their_account(
#     petstore_api, username, expected_status
# ):
#     response = petstore_api.delete(f"{USER_ENDPOINT}/{username}")
#     assert response.status == expected_status













