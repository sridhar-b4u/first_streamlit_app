import streamlit, pandas

streamlit.title('🎂My First StreamLit App')
streamlit.header('🎂Display Food List')
streamlit.text('🎂From Amazon S3')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick Some Fruits by Index:", list(my_fruit_list.index))
#my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick Some Fruits by Name:", list(my_fruit_list.set_index('Fruit').index))

streamlit.multiselect("Pick Some Fruits by Name (Choosen some default):", list(my_fruit_list.set_index('Fruit').index),['Avocado', 'Apple'])

streamlit.multiselect("Pick Some Fruits by Name (Choosen some default gave incorrect):", list(my_fruit_list.set_index('Fruit').index),['Avocado', 'Apples'])
