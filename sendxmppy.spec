%define module_name sendxmppy
Name: %module_name
Version: 0.1
Release: alt1

Summary: XMPP message sender from CLI

License: BSD
Group: Networking/Instant messaging
Url: http://git.altlinux.org/people/zver/packages/sendxmppy.git

Source: %name-%version.tar
BuildArch: noarch

%description
XMPP message sender from CLI

%prep
%setup

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Nov 25 2009 Denis Klimov <zver@altlinux.org> 0.1-alt1
- Initial build for ALT Linux

