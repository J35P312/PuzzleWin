# -*- coding: utf-8 -*-

SV_TYPES = (
    'DEL',
    'DUP',
    'INV',
    'INS',
    'CNV',
    'BND',
    'TDUP',
)


INHERITANCE_MODELS = (
    ('AR_hom', 'Autosomal Recessive Homozygote'),
    ('AR_hom_dn', 'Autosomal Recessive Homozygote De Novo'),
    ('AR_comp', 'Autosomal Recessive Compound'),
    ('AR_comp_dn', 'Autosomal Recessive Compound De Novo'),
    ('AD', 'Autosomal Dominant'),
    ('AD_dn', 'Autosomal Dominant De Novo'),
    ('XR', 'X Linked Recessive'),
    ('XR_dn', 'X Linked Recessive De Novo'),
    ('XD', 'X Linked Dominant'),
    ('XD_dn', 'X Linked Dominant De Novo'),
)

INHERITANCE_MODELS_SHORT = [model[0] for model in INHERITANCE_MODELS]

SO_TERMS = (
    'transcript_ablation',
    'splice_donor_variant',
    'splice_acceptor_variant',
    'stop_gained',
    'frameshift_variant',
    'stop_lost',
    'start_lost',
    'initiator_codon_variant',
    'transcript_amplification',
    'inframe_insertion',
    'inframe_deletion',
    'missense_variant',
    'protein_altering_variant',
    'splice_region_variant',
    'incomplete_terminal_codon_variant',
    'stop_retained_variant',
    'synonymous_variant',
    'coding_sequence_variant',
    'mature_miRNA_variant',
    '5_prime_UTR_variant',
    '3_prime_UTR_variant',
    'non_coding_exon_variant',
    'non_coding_transcript_exon_variant',
    'non_coding_transcript_variant',
    'nc_transcript_variant',
    'intron_variant',
    'NMD_transcript_variant',
    'non_coding_transcript_variant',
    'upstream_gene_variant',
    'downstream_gene_variant',
    'TFBS_ablation',
    'TFBS_amplification',
    'TF_binding_site_variant',
    'regulatory_region_ablation',
    'regulatory_region_amplification',
    'regulatory_region_variant',
    'feature_elongation',
    'feature_truncation',
    'intergenic_variant'
)

IMPACT_LEVELS = (
    'HIGH',
    'MEDIUM',
    'LOW',
)