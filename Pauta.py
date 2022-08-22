# -*- coding: utf-8 -*-
import requests
from tabulate import tabulate
import subprocess
import re
from bs4 import BeautifulSoup
import pysvn


class Pauta:
    jira_user = "jirabot:Kakaroto123"

    def __init__(self, pauta):
        self.pauta = pauta
        self.url_jira = "https://jira.afphabitat.net/browse/"
        self.url_pauta = str(self.url_jira)+str(pauta)
        self.html_pauta = self.getHtmlPauta()
        self.html_tab = self.getHtmlTab()
        #self.checkListResult = self.getCheckListCommitVersion()

    def printTab(self):
        print(tabulate(self.paths, headers=["PATH", "VERSION"]))

    def printCheckListResult(self):
        newtab = [[]]
        for x in range(len(self.paths)):
            temp = []
            temp.append(self.paths[x][0])
            temp.append(self.paths[x][1])
            temp.append(self.checkListResult[x])
            newtab.append(temp)
        del newtab[0]
        print(tabulate(newtab, headers=["PATH", "VERSION", "STATUS"]))

    def getListCommitVersion(self, branch, version):
        client = pysvn.Client()
        #client.checkout(branch, '/sql', revision=pysvn.Revision(pysvn.opt_revision_kind.number, version))

    def getListCommitVersion2(self, branch):
        p = subprocess.Popen(["svn", "--non-interactive", "--username", "prov_zt", "--password",
                             "d3liverance", "log", "-r", "1:HEAD", branch], stdout=subprocess.PIPE)
        output, err = p.communicate()
        output = re.findall("r\d+", output)
        versions = []
        for put in output:
            versions.append(put.replace('r', ''))
        return versions

    def getHtmlPauta(self):
        resp = requests.get(self.url_pauta, auth=('jirabot', 'Kakaroto123'))
        return resp.text

    def getHtmlTab(self):
        soup = BeautifulSoup(self.html_pauta, 'html.parser')

        data = []
        table = soup.find("table", attrs={"class": "confluenceTable"})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        data.pop(0)
        print(data[0][0])
        print(data[0][1])
        self.getListCommitVersion(data[0][0], data[0][1])
        return data


"""
	def getCheckListCommitVersion(self):
		result = []
		for i in range(len(self.paths)):
			try:	
				if(self.getListCommitVersion(self.paths[i][0]).index(self.paths[i][1]) >= 0):
					result.append("Ok")
			except:
				result.append("Err") 
		return result

	def getTab(self):
		path=[]
		paths=[[]]
		for tab in self.html_tab:
			for field in tab:
				a = str(field[0].replace(u'\xa0',u''))
				b = str(field[1].replace(u'\xa0',u''))
				if(a == 'Path'):
					path.append(b)
				if(a == 'Version'):
					path.append(b)
					paths.append(path)
					path=[]
		del paths[0]
		return paths



"""
