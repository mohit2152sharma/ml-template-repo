from utils.decorators import assert_shape
from utils.dir_utils import load_processed_data


def test_events_clean_shape():
    events = load_processed_data("events.pkl")
    group_by = ["user_code", "poll_code", "event", "createdAt"]
    assert_shape(group_by=group_by)(events)


def test_interactions_clean_shape():
    interactions = load_processed_data("interactions.pkl")
    group_by = ["user_code", "poll_code", "createdAt"]
    assert_shape(group_by=group_by)(interactions)


def test_users_clean_shape():
    users = load_processed_data("users.pkl")
    assert_shape(group_by=["user_code"])(users)
