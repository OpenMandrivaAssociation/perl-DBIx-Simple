%define upstream_name    DBIx-Simple
%define upstream_version 1.35

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Easy-to-use OO interface to DBI
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

