import streamlit, pandas

streamlit.title('🎂My First StreamLit App')
streamlit.header('🎂Display Food List')
streamlit.text('🎂From Amazon S3')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick Some Fruits by Index:", list(my_fruit_list.index))
streamlit.multiselect("Pick Some Fruits by Name:", list(my_fruit_list.set_index('Fruit')))

streamlit.multiselect("Pick Some Fruits by Name:", list(my_fruit_list.set_index('Fruit')),['Avacado', 'Apple'])
