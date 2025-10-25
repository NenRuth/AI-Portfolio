# A web API is a part of a website designed to interact with programs that use very specific URLs 
# to request certain information. This kind of request is called an API call.

# import requests
# # Make an API call and store the response.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)

# # Store API response in a variable.
# response_dict = r.json()
# # Process results.
# print(response_dict.keys())


# import requests
# # Make an API call and store the response.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)

# # Store API response in a variable.
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count']) #'total_count', which represents the total number of Python repositories on GitHub.

# # Explore information about the repositories.
# repo_dicts = response_dict['items'] #'items' is a list containing a number of dictionaries, each of which contains data about an individual Python repository.
# print("Repositories returned:", len(repo_dicts))

# # Examine the first repository.
# repo_dict = repo_dicts[0]  #pull out the first item from repo_dicts and store it in repo_dict. 
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])  #print the name of the project.
# print('Owner:', repo_dict['owner']['login']) #we use the key owner to access the dictionary representing the owner and then use the key login to get the owner’s login name.
# print('Stars:', repo_dict['stargazers_count']) #we print how many stars the project has earned.
# print('Repository:', repo_dict['html_url']) #the URL for the project’s GitHub repository.
# print('Created:', repo_dict['created_at']) #when it was created.
# print('Updated:', repo_dict['updated_at']) #when it was last updated. 
# print('Description:', repo_dict['description']) #print the repository’s description.


# print("\nKeys:", len(repo_dict)) #print the number of keys in the dictionary to see how much information we have. 
# for key in sorted(repo_dict.keys()):   #print all of the dictionary’s keys to see what kind of information is included.
# print(key)


#Summarizing the Top Repositories
# import requests
# # Make an API call and store the response.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)

# # Store API response in a variable.
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count']) #'total_count', which represents the total number of Python repositories on GitHub.

# # Explore information about the repositories.
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
# print('\nName:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Description:', repo_dict['description'])



#Monitoring API Rate Limits
#there’s a limit to how many requests you can make in a certain amount of time. 
#at https://api.github.com/rate_limit, this is my own limit at the time:

# {"resources":
# {"code_search":{"limit":60,
# "remaining":60,
# "reset":1761361442,
# "used":0,
# "resource":"code_search"},

# "core":{"limit":60,
# "remaining":60,
# "reset":1761361442,
# "used":0,
# "resource":"core"},

# "graphql":{"limit":0,
# "remaining":0,
# "reset":1761361442,
# "used":0,
# "resource":"graphql"},

# "integration_manifest":{"limit":5000,
# "remaining":5000,
# "reset":1761361442,
# "used":0,
# "resource":"integration_manifest"},

# "search":{"limit":10,
# "remaining":10,
# "reset":1761357902,
# "used":0,
# "resource":"search"}},

# "rate":{"limit":60,
# "remaining":60,
# "reset":1761361442,
# "used":0,
# "resource":"core"}}


#Visualizing Repositories Using Pygal
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# # Make an API call and store the response.
# URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
# r = requests.get(URL)
# print("Status code:", r.status_code)

# # Store API response in a variable.
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])

# # Explore information about the repositories.
# repo_dicts = response_dict['items']
# names, stars = [], []   #create two empty lists to store the data we’ll include in the chart.
# for repo_dict in repo_dicts:  #In the loop, we append the name of each project and number of stars it has to these lists
# 	names.append(repo_dict['name'])
# 	stars.append(repo_dict['stargazers_count'])

# # Make visualization.
# my_style = LS('#333366', base_style=LCS)  #define a style using the LightenStyle class (alias LS) and base it on a dark shade of blue w. We also pass the base_style argument to use the LightColorizedStyle class (alias LCS).
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) #use Bar() to make a simple bar chart and pass it my_style
##set the rotation of the labels along the x-axis to 45 degrees (x_label_rotation=45), and we hide the legend, because we’re plotting only one series on the chart (show_legend=False).

# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
# chart.add('', stars)
# #chart.render_to_file('python_repos.svg')

## refine the styling of the chart
# #Make visualization.
# my_style = LS('#333366', base_style=LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
# { chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')


#how you would use API calls on other sites, we’ll look at Hacker News (http://news.ycombinator.com/).
{
'url': 'http://www.bbc.co.uk/news/science-environment-33524589',
'type': 'story',
'title': 'New Horizons: Nasa spacecraft speeds past Pluto',
'descendants': 141,
'score': 230,
'time': 1436875181,
'text': '',
'by': 'nns',
'id': 9884165,
'kids': [9884723, 9885099, 9884789, 9885604, 9885844]}

#an API call that returns the IDs of the current top articles
import requests
from operator import itemgetter
# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)
# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
# Make a separate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' +
	str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
response_dict = submission_r.json()
submission_dict = {
'title': response_dict['title'],
'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
'comments': response_dict.get('descendants', 0)
}
submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])