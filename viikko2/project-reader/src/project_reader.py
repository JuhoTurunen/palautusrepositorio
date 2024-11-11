from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        serialized_content = request.urlopen(self._url).read().decode("utf-8")
        content = tomli.loads(serialized_content)["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            content["name"],
            content["description"],
            content["license"],
            content["authors"],
            content["dependencies"],
            content["group"]["dev"]["dependencies"],
        )
