def test_get_activities_returns_200_and_structure(client):
    # Arrange
    expected_keys = {"Chess Club", "Programming Class", "Gym Class"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert expected_keys.issubset(set(data.keys()))
    assert "participants" in data["Chess Club"]


def test_signup_adds_participant_and_prevents_duplicates(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup?email={email}"

    # Act
    first_response = client.post(signup_url)
    second_response = client.post(signup_url)

    # Assert
    assert first_response.status_code == 200
    assert first_response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Already signed up"


def test_remove_participant(client):
    # Arrange
    activity_name = "Programming Class"
    email = "emma@mergington.edu"
    remove_url = f"/activities/{activity_name}/participants?email={email}"

    # Act
    response = client.delete(remove_url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"
    assert email not in client.get("/activities").json()[activity_name]["participants"]
