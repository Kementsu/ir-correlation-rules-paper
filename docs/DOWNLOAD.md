# Obtaining the data

`data/raw/` is excluded from version control. This file documents how to
recreate its contents.

## 1. Chemotion IR (primary dataset)

**Chemotion Repository - Data collection: FT-IR spectroscopy data (Chemotion IR)**,
RADAR4Chem, DOI [10.22000/OGoEQGlsZGElrgst](https://doi.org/10.22000/OGoEQGlsZGElrgst),
licensed CC BY-SA 4.0, published with Punjabi et al., *Journal of Cheminformatics*
2025, 17:24, DOI [10.1186/s13321-025-00960-2](https://doi.org/10.1186/s13321-025-00960-2).

### Automated download

The DOI resolves to the RADAR4Chem landing page:

```
https://radar4chem.radar-service.eu/radar/en/dataset/OGoEQGlsZGElrgst
```

The download button on that page is driven by JavaScript, but the page embeds a
`schema.org` `DataDownload` block whose `contentUrl` is a plain HTTP resource
that can be fetched directly. It is a BagIt archive in **tar** format (not zip),
47,502,336 bytes:

```sh
curl -L -o data/raw/chemotion_ir_radar4chem_OGoEQGlsZGElrgst.tar \
  https://radar4chem.radar-service.eu/radar-backend/archives/OGoEQGlsZGElrgst/versions/1/content
```

Windows PowerShell:

```powershell
Invoke-WebRequest -UseBasicParsing `
  -Uri 'https://radar4chem.radar-service.eu/radar-backend/archives/OGoEQGlsZGElrgst/versions/1/content' `
  -OutFile 'data/raw/chemotion_ir_radar4chem_OGoEQGlsZGElrgst.tar'
```

Keep that archive unmodified. Downloading it implies accepting the RADAR terms
of use shown on the landing page, and the CC BY-SA 4.0 conditions of the dataset.

### Unpacking

The outer tar is a BagIt bag. Inside `data/dataset/` there is a second archive,
`JCAMP-DX Files/IR_data.tar.xz`, which holds the spectra:

```sh
mkdir -p data/raw/chemotion_ir
tar -xf data/raw/chemotion_ir_radar4chem_OGoEQGlsZGElrgst.tar -C data/raw/_tmp
mv data/raw/_tmp/10.22000-OGoEQGlsZGElrgst data/raw/chemotion_ir
tar -xf "data/raw/chemotion_ir/data/dataset/JCAMP-DX Files/IR_data.tar.xz" \
  -C "data/raw/chemotion_ir/data/dataset/JCAMP-DX Files"
```

The resulting layout, which `scripts/inventory.py` expects:

```
data/raw/chemotion_ir/
  bag-info.txt
  bagit.txt
  manifest-md5.txt
  tagmanifest-md5.txt
  data/
    readme.txt
    descriptive-md/
    technical-md/
    dataset/
      README.md
      meta_data.json                 2116 sample records
      JCAMP-DX Files/
        IR_data.tar.xz
        exp/                         4183 JCAMP-DX files, named by UUID
```

Notes on the layout:

- The 4183 spectrum files carry **no file extension**. They are named by the
  UUID that appears as the last segment of the `identifier` field of each
  attachment in `meta_data.json` (the `identifier` has the form `8/<uuid>`).
- Each sample contributes both a full spectrum and one or more peak tables, so
  the number of files is roughly twice the number of samples. Every one of the
  4183 attachments in `meta_data.json` has a matching file, and every file is
  referenced by the metadata.
- Chemotion writes a descending **point counter** in the X column of the XYDATA
  block rather than the wavenumber. The real axis must be reconstructed from
  `##FIRSTX`, `##LASTX` and `##NPOINTS`. The `jcamp` library does exactly this,
  but reports an "X-Check failed" warning on every line; `scripts/inventory.py`
  suppresses those.

### Manual fallback

If the direct URL stops working, open the landing page, accept the terms and use
the "Download (47.5 MB)" button, then place the downloaded archive at
`data/raw/chemotion_ir_radar4chem_OGoEQGlsZGElrgst.tar` and unpack it as above.

## 2. NIST Chemistry WebBook (replication set)

Condensed-phase IR spectra from the NIST Chemistry WebBook, DOI
[10.18434/T4D303](https://doi.org/10.18434/T4D303).

These spectra are **not redistributed** by this project and are not included in
any release. Only the list of identifiers used, the download script, and the
derived results are published. The download script is not written yet; this
section will be completed when the replication set is defined.
