provtype = 'SDV-MB'
provatstartup = "Disabled"
autosync = 0
syncnow = 'No'
ecinterfaceaddress = 'n/a'
ecinterfaceport = 80
provrequesturl = '/pksrmdevice'
provrespurl = '/sdvProvisionItemList'
sourceurl = '/source'
streamurl = '/stream'
config = {}
zero = 0
one = 1


class Variance(object):
    def __init__(self, dict):
        self.expected = dict

    def iskeyexists(self, entire):
        flag = False
        for key in self.expected:
            if key in entire:
                flag = True
            else:
                flag = False
        return flag

    def isEquals(self, entire):
        if cmp(self.expected, entire) == 0:
            return True
        else:
            return False

    def get_must_contain(self, entire):
        if self.iskeyexists(entire):
            return self.expected
        return None

    def get_variance_single(self, entire, requests=[]):
        must_contain = self.get_must_contain(entire)
        if must_contain:
            for element in entire:
                variance = {}
                if element not in must_contain:
                    for item in must_contain:
                        variance[item] = must_contain[item]
                    variance[element] = entire[element]
                    requests.append(variance)
        return requests

    def get_variance(self, entire, requests=[]):
        must_contain = self.get_must_contain(entire)
        if must_contain:
            requests.append(must_contain)
            if len(entire) > zero:
                for element_index in range(one, len(entire)):
                    if element_index is one:
                        self.get_variance_single(entire, requests)
                        continue
                    counter = zero
                    variance = {}
                    for element in entire:
                        if element not in must_contain and counter < element_index:
                            counter += 1
                            for item in must_contain:
                                variance[item] = must_contain[item]
                            variance[element] = entire[element]
                        else:
                            variance = {}
                        if variance and counter == element_index:
                            requests.append(variance)
        return requests


if __name__ == '__main__':
    config['Provision'] = {'ProvisionType': provtype,
                           'ProvAtStartup': provatstartup,
                           'AutoSync': autosync,
                           'SyncNow': syncnow,
                           'ECInterfaceAddress': ecinterfaceaddress,
                           'ECInterfacePort': ecinterfaceport,
                           'ProvisionReqURL': provrequesturl,
                           'ProvisionRespURL': provrespurl,
                           'SourceURL': sourceurl,
                           'StreamURL': streamurl
                           }
    expected = Variance({'ProvAtStartup': 'Enabled'})
    requests_variance = expected.get_variance(config['Provision'])
    for input in requests_variance:
        print(input)
