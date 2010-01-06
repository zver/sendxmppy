%define module_name sendxmppy
Name: %module_name
Version: 0.4
Release: alt1

Summary: XMPP message sender from CLI

License: BSD
Group: Networking/Instant messaging
Url: http://git.altlinux.org/people/zver/packages/sendxmppy.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-dev

Requires: python-module-jabberpy

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
* Wed Jan 06 2010 Denis Klimov <zver@altlinux.org> 0.4-alt1
- new version

* Mon Jan 04 2010 Denis Klimov <zver@altlinux.org> 0.3-alt2
- add require to python-module-jabberpy (Closes: #22678)

* Sun Dec 13 2009 Denis Klimov <zver@altlinux.org> 0.3-alt1
- new version

* Sat Nov 28 2009 Denis Klimov <zver@altlinux.org> 0.2-alt2
- add build require to python-dev

* Wed Nov 25 2009 Denis Klimov <zver@altlinux.org> 0.2-alt1
- new version

* Wed Nov 25 2009 Denis Klimov <zver@altlinux.org> 0.1-alt1
- Initial build for ALT Linux

