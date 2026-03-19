from edgar import Company, get_filings

# # Set your SEC user identity first (required by the SEC)
# # Replace with your name and email
from edgar import set_identity 
set_identity("Your Name your.email@example.com") 

# # Get filings for a company, convert to pandas DataFrame
# # company = Company.get_ticker("SNOW")
# # # company = Company.for_ticker("SNOW") 
# # filings = company.get_filings(form=["10-K", "10-Q"]) # get specific forms
# # filings_df = filings.to_pandas() # convert to pandas DataFrame

# # # Export the DataFrame to a JSON file
# # filings_df.to_json("filings.json", orient="records", date_format="iso")


# berkshire = Company("BRK.A")

# filing = berkshire.get_filings(form="13F-HR").latest(1)
# report = filing.obj()

# # print(report)


# # from edgartools import filings


# # # Filter for 10-K filings
# # ten_k_filings = filing.filter(form="10-K")

# # print(ten_k_filings)


# # # Convert to JSON
# # ten_k_filings.to_json("sp500_10k_2020_2023.json")

# filings = get_filings(range(2020, 2024)).get_filing_at

# print(filings)


# from edgar import Company

# fund = Company("VANGUARD INDEX FUNDS")
# nport = fund.get_filings(form="NPORT-P")[0].obj()
# nport.investments  # Full holdings


# company = Company("JPM").get_filings(form="13F-HR")

# for i in range(100):
    
#     print(company.get_filing_at(i))


from edgar import Company

filings = Company("JPM").get_filings(form="13F-HR")

print("#", "filing date", "total value", "total holdings")

for i in range(min(100, len(filings))):
    filing = filings[i]              
    report = filing.obj()            

    print(
        i,
        filing.filing_date,
        report.total_value,          
        report.total_holdings        
    )
