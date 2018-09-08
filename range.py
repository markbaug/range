def smaller(numa,numb):
	if numa<=numb:
		return numa
	if numb<=numa:
		return numb
def smallest(numa,numb,numc):
	small=smaller(numa,numb)
	tiny=smaller(small,numc)
	return tiny
def bigger(numa,numb):
	if numa>=numb:
		return numa
	if numb>=numa:
		return nummb
def biggest(numa,numb,numc):
	larger=bigger(numa,numb)
	largest=bigger(larger,numc)
	return largest
def set_range(numa,numb,numc):
	largest=biggest(numa,numb,numc)
	tiny=smallest(numa,numb,numc)
	range=largest-tiny
	return range