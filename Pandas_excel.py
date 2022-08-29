import  pandas as pd

inv_file = pd.read_excel('inventory.xlsx',sheet_name = 'Sheet1')
#print(inv_file.cell(1,1).value)
#print(inv_file.head(78))

no_of_record =  len(inv_file)
print(no_of_record)

for record in range( 0, no_of_record ):

    if inv_file['Inventory'].iloc[record] == 20 :
        print(f"product no - {inv_file['Product No'].iloc[record]} No of Inventory - {int(inv_file['Inventory'].iloc[record])}")
