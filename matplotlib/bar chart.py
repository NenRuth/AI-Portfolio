#Making a Histogram/bar chart

# import matplotlib.pyplot as plt

# # Sample data
# languages = ['Python', 'JavaScript', 'C++', 'Java']
# popularity = [90, 80, 70, 60]

# # Create a bar chart
# plt.bar(languages, popularity, color='skyblue')

# # Add a title and labels
# plt.title('Programming Language Popularity')
# plt.xlabel('Languages')
# plt.ylabel('Popularity Score')

# # Display the chart
# #plt.savefig('bar1')
# plt.show()


# import pygal

# languages = ['Python', 'JavaScript', 'C++', 'Java']
# popularity = [90, 80, 70, 60]

# bar_chart = pygal.Bar()
# bar_chart.title = 'Programming Language Popularity (Pygal)'
# bar_chart.x_labels = languages
# bar_chart.add('Popularity', popularity)

# # Save as an interactive SVG
# bar_chart.render_to_file('pygal_chart.svg')
# #print("Chart saved as pygal_chart.svg")

# # Optional: automatically open in browser
# import webbrowser, os
# webbrowser.open('file://' + os.path.realpath('pygal_chart.svg'))




#line_chart
# import pygal
# line_chart = pygal.Line()
# line_chart.title = 'Monthly Temperature'
# line_chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr']
# line_chart.add('2025', [25, 28, 31, 33])
# line_chart.add('2024', [24, 27, 29, 30])
# line_chart.render_to_file('temperature_line_chart.svg')

# import webbrowser, os
# webbrowser.open('file://' + os.path.realpath('pygal_chart.svg'))


# import pygal
# import webbrowser, os

# # Create a Line Chart
# line_chart = pygal.Line()
# line_chart.title = 'Monthly Temperature'
# line_chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr']

# # Add data for two years
# line_chart.add('2025', [25, 28, 31, 33])
# line_chart.add('2024', [24, 27, 29, 30])

# # Save the chart as an SVG file
# file_name = 'temperature_line_chart.svg'
# line_chart.render_to_file(file_name)

# #Show where the file was saved
# print("Chart saved at:", os.path.abspath(file_name))

# # Automatically open it in your browser
# webbrowser.open('file://' + os.path.realpath(file_name))


# import pygal
# import webbrowser, os

# # Create a Line Chart
# line_chart = pygal.Line()
# line_chart.title = 'Monthly Temperature'
# line_chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr']

# # Add data for two years
# line_chart.add('2025', [25, 28, 31, 33])
# line_chart.add('2024', [24, 27, 29, 30])
# line_chart.add('2023', [20, 17, 29, 10])

# # Save the chart as an SVG file
# file_name = 'temperature1_line_chart.svg'
# line_chart.render_to_file(file_name)

# # Show where the file was saved
# #print("Chart saved at:", os.path.abspath(file_name))

# # Automatically open it in your browser
# webbrowser.open ('file://' + os.path.realpath(file_name))


# pie_chart
# import pygal
# import webbrowser, os

# # Create a Pie chart
# pie_chart = pygal.Pie()
# pie_chart.title = 'Market Share of Mobile Operating Systems (2025)'

# # Add data (label, value)
# pie_chart.add('Android', 70)
# pie_chart.add('iOS', 25)
# pie_chart.add('Others', 5)

# # Save the chart as an SVG file
# file_name = 'mobile_os_share.svg'
# # line_chart.render_to_file(file_name)
# pie_chart.render_to_file('file_name')

# print("Pie chart saved successfully as 'mobile_os_share.svg'")

# webbrowser.open ('file://' + os.path.realpath(file_name))


# import pygal

# pie_chart = pygal.Pie()
# pie_chart.title = 'Market Share of Mobile Operating Systems (2025)'
# pie_chart.add('Android', 70)
# pie_chart.add('iOS', 25)
# pie_chart.add('Others', 5)

# pie_chart.render_to_file('mobile_os_share.svg')

