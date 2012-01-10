%define		php_min_version 5.0.0
%define		pkgname	restructuredtext
%include	/usr/lib/rpm/macros.php
Summary:	Parser to convert reStructuredText files to HTML using PHP
Name:		php-%{pkgname}
Version:	0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	https://php-restructuredtext.googlecode.com/files/php-restructuredtext-%{version}.tar.gz
# Source0-md5:	1883a90574efabbb9e5fe8b90fa82b5d
URL:		https://code.google.com/p/php-restructuredtext/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bad depsolver
%define		_noautopear	pear
# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
This is a simple, incomplete (but functional) alternative to python
parsers of restructuredtext usign only PHP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p rst.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p test.php ceferino_cara.png $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%{php_data_dir}/rst.php
%{_examplesdir}/%{name}-%{version}
