%define	module	DBIx-Simple
%define	modver	1.35

Summary:	Easy-to-use OO interface to DBI
Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{module}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(DBI)
BuildRequires:	perl-devel

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

This module is aimed at rapid development and easy maintenance. Query
preparation and execution are combined in a single method, the result
object (which is a wrapper around the statement handle) provides easy
row-by-row and slurping methods.

The 'query' method returns either a result object, or a dummy object. The
dummy object returns undef (or an empty list) for all methods and when used
in boolean context, is false. The dummy object lets you postpone (or skip)
error checking, but it also makes immediate error checking simply
'$db->query(...) or die $db->error'.

%prep
%setup -qn %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

