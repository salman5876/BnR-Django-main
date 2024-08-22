request['SNR_Title'] = parseHtml(request['SNR_Title'])
request["SNR_Description"] = parseHtml(request["SNR_Description"])
request['SNR_CustomerReviews'] = float("%0.2f" % request['SNR_CustomerReviews'])
request['SNR_Price'] = float("%0.2f" % request['SNR_Price'])
request["SNR_PriceBefore"] = float("%0.2f" % request["SNR_PriceBefore"])
try:
    request["SNR_Category"] = map_data(cap_dict, request["SNR_Category"])
except:
    pass
yield request
