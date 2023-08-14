import argparse
import gitlab
import sys

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Delete member from all accessible gitlab projects.')
    parser.add_argument('--query', required=True,
                        help='Gitlab query string that defines users '
                        'to be deleted (username is recommended)')
    parser.add_argument('--token', required=True,
                        help='Gitlab token of your user')
    parser.add_argument('--url', default='https://gitlab.com',
                        help='Gitlab URL')
    parser.add_argument('--visibility', default='private',
                        help='Gitlab projects visibility')
    parser.add_argument('--dry', action='store_true',
                        help='dry run')
    return parser.parse_args()


def print_ok():
    """Print fancy ok message."""
    print('🟢 ok')


def print_fail():
    """Print fancy fail message."""
    print('🔴 fail')


def print_skip():
    """Print fancy skip message."""
    print('🟡 skip')


def main():
    """Script entry point."""
    args = parse_args()

    print(f'💬 Auth to {args.url} : ', end='')
    gl = gitlab.Gitlab(args.url, private_token=args.token)
    try:
        gl.auth()
        print_ok()
    except:
        print_fail()
        sys.exit(1)
        return

    projects = gl.projects.list(all=True, visibility=args.visibility)
    for p in projects:
        print(f'Project "{p.name_with_namespace}"')
        usrlist = args.query
        for i in usrlist.split(","):
            members = p.members.list(query=i)
            if len(members) == 0:
                print(' {} not found'.format(i))
            else:
                for member in members:
                    if (member.username) == i:
                        print(f' delete {member.username} (id={member.id}) : ', end='')
                        if not args.dry:
                            try:
                                member.delete()
                                print_ok()
                            except:
                                print_fail()
                        else:
                            print_skip()
                    else:
                        print(' {} not found'.format(i))

    print(f'💬 Done ')

if __name__ == '__main__':
    main()
