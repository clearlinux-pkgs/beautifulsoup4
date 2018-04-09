#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beautifulsoup4
Version  : 4.6.0
Release  : 35
URL      : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.6.0.tar.gz
Source0  : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.6.0.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: beautifulsoup4-python3
Requires: beautifulsoup4-python
Requires: html5lib
Requires: lxml
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
= Introduction =
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
>>> print soup.prettify()
<html>
<body>
<p>
Some
<b>
bad
<i>
HTML
</i>
</b>
</p>
</body>
</html>
>>> soup.find(text="bad")
u'bad'

%package python
Summary: python components for the beautifulsoup4 package.
Group: Default
Requires: beautifulsoup4-python3

%description python
python components for the beautifulsoup4 package.


%package python3
Summary: python3 components for the beautifulsoup4 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523286132
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
