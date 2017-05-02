#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beautifulsoup4
Version  : 4.5.3
Release  : 27
URL      : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.5.3.tar.gz
Source0  : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.5.3.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: beautifulsoup4-python
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

%description python
python components for the beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.5.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484533840
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484533840
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
