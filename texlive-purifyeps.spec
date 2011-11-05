# revision 20636
# category Package
# catalog-ctan /support/purifyeps
# catalog-date 2009-03-25 09:03:02 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-purifyeps
Version:	1.0a
Release:	1
Summary:	Make EPS work with both LaTeX/dvips and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/purifyeps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-purifyeps.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/purifyeps
%{_texmfdistdir}/scripts/purifyeps/purifyeps
%doc %{_texmfdistdir}/doc/support/purifyeps/README
%doc %{_mandir}/man1/purifyeps.1*
%doc %{_texmfdir}/doc/man/man1/purifyeps.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
