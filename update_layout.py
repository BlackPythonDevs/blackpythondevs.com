import typing
import typer
import pathlib
import frontmatter


app = typer.Typer(no_args_is_help=True)


@app.command(name="check")
def check_file(
    target_files: typing.List[pathlib.Path],
) -> None:
    """Check a file for the layout attribute"""

    ret_code = 0
    for target_file in target_files:
        fm_file = frontmatter.loads(target_file.read_text())

        if "layout" not in fm_file.metadata:
            print("%s is missing the `layout` value. Applying layout: post.")
            fm_file["layout"] = "post"
            target_file.write_text(frontmatter.dumps(fm_file))
            ret_code = 1

    typer.Exit(code=ret_code)


if __name__ == "__main__":
    app()
