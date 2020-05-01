# 2
import pandas as pd

# 3
# Read each state's government measures data into separate DataFrames 
ct_df = pd.read_csv('Outputs/ct.csv', encoding='utf8')
ma_df = pd.read_csv('Outputs/ma.csv', encoding='utf8')
vt_df = pd.read_csv('Outputs/vt.csv', encoding='utf8')
ri_df = pd.read_csv('Outputs/ri.csv', encoding='utf8')
nh_df = pd.read_csv('Outputs/nh.csv', encoding='utf8')
me_df = pd.read_csv('Outputs/me.csv', encoding='utf8')
print('DataFrame for Connecticut')
print(ct_df.head(5))
print('DataFrame for Massachusetts')
print(ma_df.head())
print('DataFrame for Vermont')
print(vt_df.head())
print('DataFrame for Rhode Island')
print(ri_df.head())
print('DataFrame for New Hampshire')
print(nh_df.head())
print('DataFrame for Maine')
print(me_df.head())
print('\n')

# 4
# Check the datatype of each column
print('Datatypes for Connecticut')
datatypes_ct = ct_df.dtypes
print(datatypes_ct)
print('Datatypes for Massachusetts')
datatypes_ma = ma_df.dtypes
print(datatypes_ma)
print('Datatypes for Vermont')
datatypes_vt = vt_df.dtypes
print(datatypes_vt)
print('Datatypes for Rhode Island')
datatypes_ri = ri_df.dtypes
print(datatypes_ri)
print('Datatypes for New Hampshire')
datatypes_nh = nh_df.dtypes
print(datatypes_nh)
print('Datatypes for Maine')
datatypes_me = me_df.dtypes
print(datatypes_me)
print('\n')

# 5
# Sorting by date and show the top 15 entries in descending order
print('Sorting by Date')
print(ct_df.sort_values('Date', ascending=False).head(15))
print('\n')

# 6a
# Remove the PDF Order Link column from the DataFrame
print('Horizontal Slicing')
filter_columns = ['Date', 'Description']
vertically_filtered_ct_df = ct_df[filter_columns]
print(vertically_filtered_ct_df.head(15))
print('\n')

# 6b
# Remove any data entries with dates after March 31st, 2020 from the DataFrame
print('Vertical Slicing')
filter_date = '03/31/2020'
horizontally_filtered_ct_df = ct_df[ct_df['Date'] < filter_date]
print(horizontally_filtered_ct_df.head(15))
print('\n')

# 7
# Merge 2 DataFrames
print('Outer Merge')
outer_join = pd.merge(ct_df, vt_df, how='outer')
print(outer_join)

print('Left Merge')
left_join = pd.merge(ct_df, vt_df, how='left')
print(left_join)

# 8
# Save the outer and left merges to JSON
outer_join.to_json('ct-vt-outer.json', orient='columns')
left_join.to_json('ct-vt-left.json', orient='columns')
