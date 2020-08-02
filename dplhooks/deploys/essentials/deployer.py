import os
import shutil
import subprocess
from pathlib import Path

from dplhooks.deploys.essentials.conf_parser import ConfigurationParser


class ContainerDeployer:
    def __init__(self, workdir='~/projects', confdir='.conf'):
        Path(workdir).mkdir(parents=True, exist_ok=True)
        self.workdir = workdir
        self.confdir = confdir

    def deploy(self, project_name):
        config = ConfigurationParser(self.confdir)
        project = config.get_project(project_name)
        project_dir = f'{self.workdir}/{project_name}'
        if os.path.isdir(project_dir):
            subprocess.run(['git', 'pull'], cwd=project_dir)
        else:
            subprocess.run(['git', 'clone', project['repository'], project_name], cwd=self.workdir)
        self.copy_envfiles(project, project_dir)
        subprocess.run(['docker-compose', 'build'], cwd=project_dir)
        subprocess.run(['docker-compose', 'up', '--no-deps', '-d'], cwd=project_dir)

    def copy_envfiles(self, project, project_dir):
        envfiledir = f'{self.confdir}/envfiles'
        if 'envfiles' in project:
            for file in project['envfiles']:
                shutil.copyfile(f'{envfiledir}/{file}', project_dir)
