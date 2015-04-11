class CreditCard(object):

	def __init__(self, number, exp_month, exp_year, cvc, name=None, addressCity=None, addressCountry=None, addressLine1=None, addressLine2=None, addressState=None, addressZip=None):
		self.number = number # [min length: 13, max length: 19]
		self.exp_year = exp_year # [max value: 99]
		self.exp_month = exp_month # [min value: 1, max value: 12]
		self.cvc = cvc
		self.name = name #[min length: 2, max length: 50]
		self.addressState = addressState
		self.addressCity = addressCity
		self.addressCountry = addressCountry
		self.addressLine1 = addressLine1
		self.addressLine2 = addressLine2
		self.addressState = addressState
		self.addressZip = addressZip

	def to_simplify_obj(self):
		sobj = { 
			'number': self.number,
			'expMonth': self.exp_month,
			'expYear': self.exp_year,
			'cvc':self.cvc
			}

		if self.name:
			sobj['name'] = self.name
		if self.addressState:
			sobj['addressState'] = self.addressState
		if self.addressCity:
			sobj['addressCity'] = self.addressCity
		if self.addressCountry:
			sobj['addressCountry'] = self.addressCountry
		if self.addressLine1:
			sobj['addressLine1'] = self.addressLine1
		if self.addressLine2:
			sobj['addressLine2'] = self.addressLine2
		if self.addressState:
			sobj['addressState'] = self.addressState
		if self.addressZip:
			sobj['addressZip'] = self.addressZip

		return sobj

def test_to_simplify_obj():
	card = CreditCard(number = '5105105105105100', exp_month='06' , exp_year='20', cvc='123')
	print card.to_json()

if __name__ == "__main__":
	test_to_simplify_obj()