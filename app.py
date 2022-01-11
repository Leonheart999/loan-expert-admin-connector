from datetime import timedelta, datetime, date
import requests
import Constants
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def send_company_stats(date_from, date_to):
	p = {"dateFrom": date_from, "dateTo": date_to}
	r1 = requests.get(Constants.loanExpertCustomerStatsUrl.__str__(), p)
	if r1.ok:
		customer_stat = r1.json()
		r2 = requests.get(Constants.loanExpertStatsPortfolioUrl.__str__(), p)
		if r2.ok:
			loan_expert_portfolios = r2.json()['data']
			customer_stat['data']['loanExpertPortfolios'] = loan_expert_portfolios
			customer_stat['data']['year'] = date_to.year
			customer_stat['data']['month'] = date_to.month
			r3 = requests.post(Constants.adminStatsUrl, json=customer_stat)
			if r3.ok:
				print(r3)
			else:
				print(r3)
		else:
			return
	else:
		return

	# requests.post('https://httpbin.org / post', data ={'key':'value'})
	return


def scheduled_task():
	r = requests.get(Constants.loanExpertUniqueIdUrl.__str__())
	unique_id = r.text
	r = requests.get(Constants.adminStatsUrl, {'uniqueId': unique_id})
	date_list = r.json()['data']
	for pair in date_list:
		send_company_stats(date.fromtimestamp(pair['first']/1000), date.fromtimestamp(pair['second']/1000))
	return


scheduled_task()
scheduler.add_job(scheduled_task, 'interval', hours=int(Constants.runningTime))
scheduler.start()
# send_company_stats(,
# 				   datetime.strptime("2100-11-14", Constants.dateDefaultFormat))
