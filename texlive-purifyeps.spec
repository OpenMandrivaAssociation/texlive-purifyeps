Name:		texlive-purifyeps
Version:	29725
Release:	2
Summary:	Make EPS work with both LaTeX/dvips and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/purifyeps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-purifyeps.bin = %{EVRD}

%description
While pdfLaTeX has a number of nice features, its primary
shortcoming relative to standard LaTeX+dvips is that it is
unable to read ordinary Encapsulated PostScript (EPS) files,
the most common graphics format in the LaTeX world. Purifyeps
converts EPS files into a 'purified' form that can be read by
both LaTeX+dvips and pdfLaTeX. The trick is that the standard
LaTeX2e graphics packages can parse MetaPost-produced EPS
directly. Hence, purifyeps need only convert an arbitrary EPS
file into the same stylized format that MetaPost outputs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/purifyeps
%{_texmfdistdir}/scripts/purifyeps/purifyeps
%doc %{_mandir}/man1/purifyeps.1*
%doc %{_texmfdistdir}/doc/man/man1/purifyeps.man1.pdf
%doc %{_texmfdistdir}/doc/support/purifyeps/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
