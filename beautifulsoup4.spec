#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beautifulsoup4
Version  : 4.7.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/80/f2/f6aca7f1b209bb9a7ef069d68813b091c8c3620642b568dac4eb0e507748/beautifulsoup4-4.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/f2/f6aca7f1b209bb9a7ef069d68813b091c8c3620642b568dac4eb0e507748/beautifulsoup4-4.7.1.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: beautifulsoup4-license = %{version}-%{release}
Requires: beautifulsoup4-python = %{version}-%{release}
Requires: beautifulsoup4-python3 = %{version}-%{release}
Requires: html5lib
Requires: lxml
Requires: soupsieve
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest
BuildRequires : soupsieve

%description
Beautiful Soup is a Python package for parsing HTML and XML documents.

%package license
Summary: license components for the beautifulsoup4 package.
Group: Default

%description license
license components for the beautifulsoup4 package.


%package python
Summary: python components for the beautifulsoup4 package.
Group: Default
Requires: beautifulsoup4-python3 = %{version}-%{release}

%description python
python components for the beautifulsoup4 package.


%package python3
Summary: python3 components for the beautifulsoup4 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546992065
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/beautifulsoup4
cp COPYING.txt %{buildroot}/usr/share/package-licenses/beautifulsoup4/COPYING.txt
cp LICENSE %{buildroot}/usr/share/package-licenses/beautifulsoup4/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/beautifulsoup4/COPYING.txt
/usr/share/package-licenses/beautifulsoup4/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
