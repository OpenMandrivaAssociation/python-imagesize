%bcond_with tests

Summary:	Python library for determining image sizes

Name:		python-imagesize
Version:	1.4.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/a7/84/62473fb57d61e31fef6e36d64a179c8781605429fd927b5dd608c997be31/imagesize-1.4.1.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/imagesize
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python-pkg-resources
Obsoletes:	python2-imagesize < %{EVRD}

%description
Python library for determining image sizes

%files
%{py_puresitedir}/*
