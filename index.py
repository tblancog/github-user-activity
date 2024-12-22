import requests
import sys

def get_activity(json):
  for activity in json:
    if not activity:
      continue
    if activity['type'] == 'PushEvent':
      print(f"- Pushed {len(activity['payload']['commits'])} commits to {activity['repo']['name']}")
    elif activity['type'] == 'CreateEvent':
      print(f"- Created a new repository {activity['repo']['name']}")
    elif activity['type'] == 'WatchEvent':
      print(f"- Starred repository {activity['repo']['name']}")
    

def main():
  print(sys.argv)
  if len(sys.argv) < 3 or sys.argv[1] != 'gh-user-activity' or sys.argv[2] == '':
    print(f"Should enter: gh-user-activity <username>")
    return
  
  username = sys.argv[2]
  response = requests.get(f"https://api.github.com/users/{username}/events")
  if(response.status_code == 404):
    raise Exception(f"User '{username}' not found.")
  elif response.status_code != 200:
    raise Exception("Something went wrong.")
  
  get_activity(response.json())

if __name__ == '__main__':
  main()