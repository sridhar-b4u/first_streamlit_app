import streamlit, pandas

streamlit.title('🎂My First StreamLit App')
streamlit.header('🎂Display Food List')
streamlit.text('🎂From Amazon S3')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.text('List shown by default Index')
streamlit.multiselect("Pick Some Fruits by Index:", list(my_fruit_list.index))

#reset index of dataframe to Fruit column
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.text('List shown with Fruit column Index')
streamlit.multiselect("Pick Some Fruits by Name:", list(my_fruit_list.index))

streamlit.text('List shown with some default Fruit pre-added. This could be removed')
fruit_selected = streamlit.multiselect("Pick Some Fruits by Name (Choosen some default):", list(my_fruit_list.index),['Avocado', 'Apple'])

