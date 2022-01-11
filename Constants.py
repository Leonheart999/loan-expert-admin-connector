import configparser
import Models

dateDefaultFormat = '%Y-%m-%d'
config = configparser.ConfigParser()
config.read("ConfigFile.properties")
loanExpertHost = config["Loan Expert"]["loan-expert.host"]
loanExpertPort = config["Loan Expert"]["loan-expert.port"]
loanExpertUniqueIdPath = config["Loan Expert"]["loan-expert.unique_id.path"]
loanExpertCustomerStatsPath = config["Loan Expert"]["loan-expert.customer-stats.path"]
loanExpertStatsPortfolioPath = config["Loan Expert"]["loan-expert.stats-portfolio.path"]
loanExpertUniqueIdUrl = Models.URL(loanExpertHost, loanExpertPort, loanExpertUniqueIdPath)
loanExpertCustomerStatsUrl = Models.URL(loanExpertHost, loanExpertPort, loanExpertCustomerStatsPath)
loanExpertStatsPortfolioUrl = Models.URL(loanExpertHost, loanExpertPort, loanExpertStatsPortfolioPath)
adminHost = config["Admin"]["admin.host"]
adminPort = config["Admin"]["admin.port"]
adminStatsPath = config["Admin"]["admin.stats.path"]
adminStatsUrl = Models.URL(adminHost, adminPort, adminStatsPath)
runningTime = config["Utils"]["run-time"]
