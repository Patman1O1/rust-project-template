# Builtin Imports
import sys
import os

# Pip Imports
from jinja2 import Environment, Template, FileSystemLoader

class Project(object):
    def __init__(self, argv: list[str]) -> None: # raises ValueError
        if len(argv) < 3:
            raise ValueError(f"Usage {argv[0]} <project_name> {{Library|Executable}}")

        self.name = argv[1]
        self.type = argv[2]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name: str = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None: # raises ValueError
        if value != "Executable" and value != "Library":
            raise ValueError(f"Expected 'value' to be 'Executable' or 'Library' but got '{value}'")
        self._type: str = value

    def render(self) -> None:
        # Set the environment
        env: Environment = Environment(loader=FileSystemLoader(os.getcwd()))

        # Get the templates
        cargo_template: Template = env.get_template("Cargo.toml.j2")
        src_template: Template = env.get_template("src/{{ project.name }}.rs.j2")
        
        # Render the Cargo.toml.j2 template
        with open("Cargo.toml.j2", "w", encoding="utf-8") as cargo_file:
            cargo_file.write(cargo_template.render(project=self))

        # Rename Cargo.toml.j2 to Cargo.toml
        os.rename("Cargo.toml.j2", "Cargo.toml")

        # Render the source file template
        with open("src/{{ project.name }}.rs.j2", "w", encoding="utf-8") as src_file:
            src_file.write(src_template.render(project=self))

        # Rename "src/{{ project.name }}.rs.j2" to "src/<project_name>.rs" where <project_name> is the .name property
        if self.type == "Executable":
            os.rename("src/{{ project.name }}.rs.j2", "src/main.rs")
        else:
            os.rename("src/{{ project.name }}.rs.j2", f"src/{self.name}.rs")

def main() -> int:
    try:
        project: Project = Project(sys.argv)
        project.render()
        return 0
    except Exception as exception:
        os.write(os.STDERR_FILENO, str(f"{exception}\n").encode("utf-8"))
        return 1

if __name__ == "__main__":
    sys.exit(main())

