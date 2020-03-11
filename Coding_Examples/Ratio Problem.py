fee_in_pound = 300
fee_in_pkr = 0
transaction_fee_ration = 9  # its in percentage

transaction_fee_in_pounds = (300 * transaction_fee_ration) // 100
total_fee_in_pounds_including_transaction_fee = fee_in_pound + transaction_fee_in_pounds

fee_in_pkr = total_fee_in_pounds_including_transaction_fee * 204.34

print("Transaction Fee in PKR ",transaction_fee_in_pounds * 204.34)
print("Total Fee in PKR ",fee_in_pkr)