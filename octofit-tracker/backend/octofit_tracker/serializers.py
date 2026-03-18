from rest_framework import serializers

# User serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    team = serializers.CharField(max_length=100, required=False)

# Team serializer
class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=150))

# Activity serializer
class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=150)
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateTimeField()

# Leaderboard serializer
class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=150)
    score = serializers.IntegerField()

# Workout serializer
class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    difficulty = serializers.CharField(max_length=50)
