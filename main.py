from ui.ui import UI
from service.Service import Service
from repository.Repository import Repository
repo=Repository("data/input.gml")
serv=Service(repo)
ui=UI(serv)
ui.run()