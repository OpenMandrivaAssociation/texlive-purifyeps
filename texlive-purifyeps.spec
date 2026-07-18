%global tl_name purifyeps
%global tl_revision 79618
%global tl_bin_links purifyeps:%{_texmfdistdir}/scripts/purifyeps/purifyeps

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Make EPS work with both LaTeX/dvips and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/purifyeps
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/purifyeps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(purifyeps.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
While pdfLaTeX has a number of nice features, its primary shortcoming
relative to standard LaTeX+dvips is that it is unable to read ordinary
Encapsulated PostScript (EPS) files, the most common graphics format in
the LaTeX world. Purifyeps converts EPS files into a 'purified' form
that can be read by both LaTeX+dvips and pdfLaTeX. The trick is that the
standard LaTeX2e graphics packages can parse MetaPost-produced EPS
directly. Hence, purifyeps need only convert an arbitrary EPS file into
the same stylized format that MetaPost outputs.

