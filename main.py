
def main(f):
    print("S&P500 COMPOUNDING SIMULATOR", file=f)
    print("-------------------------------------\n", file=f)
    invest_month = input("QA: How much are you expected to invest every month: ")
    print(f"Invested per month: {invest_month}", file=f)
    print(f"You will invest {int(invest_month)*12} annually", file=f)
    annual_rentability = input("QA: How much the index (S&P500) is expected to return annually (+ dividends) '%': ")
    print(f"Expected annual rentability: {annual_rentability}", file=f)
    years_range = input("QA: Top Limit of years range: ")
    print(f"Years range: {years_range}", file=f)
    print("", file=f)

    compounded = 0
    total_invested=0
    for year in range(int(years_range)):
        next_compounded = calculate_year(compounded, year, float(invest_month), float(annual_rentability))
        total_invested = int(invest_month)*12*(year+1)
        print(f"{year+1} | {next_compounded}   (invested: {total_invested}, year return: {round(next_compounded - (compounded + (int(invest_month)*12)), 2)})", file=f)
        compounded = next_compounded

    print(f"\nTotal Returned over the years: {round(compounded - total_invested, 2)}", file=f)

    print("Check output.txt")
def calculate_year(compounded, year, invest_month, annual_rentability):
    # Method of operation: personally I think is the most accurate way of calculation
    #   1. Iterate over every month of the year
    #   2. Add the fixed invested in month to the compounded
    #   3. Rentability of the month (this is the tricky part), we're going to suppose that every month we get an
    #      equitative portion of return based on the annual rentability (p.e. 10% / 12 = 0,83% increment every month)

    for _ in range(12):
        compounded = compounded + invest_month
        compounded = compounded + (compounded*((annual_rentability/100)/12))

    # This is commented if we wanted to compound based on the total annual invested and annual rentability, this is not
    # realistic because we are funding the wallet every month and not at an annual rate.

    # compounded = compounded + (compounded*(annual_rentability/100))
    return round(compounded, 2)


if __name__ == "__main__":
    with open("output.txt", "w") as f:
        main(f)