from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
# from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC, MeltingTemp


def read_fasta(fp):
    name, seq = None, []
    for line in fp.split():
        # line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


def mk_seqrecord(x):
    result = []
    for name, seq in x:
        result.append(SeqRecord(Seq(seq), id=name))
    return result


# with open('f.fasta') as fp:
#     for name, seq in read_fasta(fp):
#         print(name, seq)


def Alignment(target_seq, query_seq):
    '''
    Read template Fasta file: should be ATG to TAG
    '''
    name, seq = None, []
    for line in target_seq.split():
        if line.startswith(">"):
            name, seq = line[1:], []
        else:
            seq.append(line)

    target_DNA = SeqRecord(Seq(''.join(seq)), id=name)
    target_Protein = target_DNA.translate()

    # simple file write
    with open('static/alignment_result.txt', 'w') as f:
        f.write('#### Life_is_Short,Use_Python. \n')
        f.write('\n')  # add blank line
        # Simple FASTA parsing
        for seq_record in mk_seqrecord(read_fasta(query_seq)):
            # print('#### DNA alignments of {} ####'.format(seq_record.id))
            f.write('#### {} foward DNA sequence alignments ####\n'.format(
                seq_record.id))
            alignments = pairwise2.align.localms(seq_record.seq,
                                                 target_DNA.seq, 2, -3, -2, -2)
            # print(pairwise2.format_alignment(*alignments[0]))
            f.write(pairwise2.format_alignment(*alignments[0]))
            f.write('#### {} reverse DNA sequence alignments ####\n'.format(
                seq_record.id))
            rev_seq = seq_record.reverse_complement()
            rev_alignments = pairwise2.align.localms(
                rev_seq.seq, target_DNA.seq, 2, -3, -2, -2)
            f.write(pairwise2.format_alignment(*rev_alignments[0]))
            f.write('\n')  # add blank line
            # print('#### Protein alignments of {} ####'.format(seq_record.id))
            f.write('#### Protein sequence alignments :  {} ####\n'.format(
                seq_record.id))
            f.write('\n')  # add blank line
            # stop codon = *, all frame shift
            forward_1 = seq_record.seq[0::].translate()
            forward_2 = seq_record.seq[1::].translate()
            forward_3 = seq_record.seq[2::].translate()
            reverse_1 = seq_record.seq[:0:-1].translate()  # reverse frame
            reverse_2 = seq_record.seq[:1:-1].translate()
            reverse_3 = seq_record.seq[:2:-1].translate()
            # make list for loop
            protein_seq = [
                forward_1, forward_2, forward_3, reverse_1, reverse_2,
                reverse_3
            ]
            # alginments
            for i in protein_seq:
                # print frame name?
                pro_alignments = pairwise2.align.localms(
                    i, target_Protein.seq, 2, -3, -2, -2)
                # print pairwise2.format_alignment(*pro_alignments[0])
                # print 1st alignments
                f.write(pairwise2.format_alignment(*pro_alignments[0]))
            f.write('\n')  # add blank line


def Oligo(target_dna):
    '''
    return should be dict type, GC_contents, Tm_value, Reverse compliment
    '''
    result = {
        'GC_contents': 0,
        'Tm_value': 0,
        'Complement_seq': 0,
        'Reverse_complement_seq': 0,
        'Length_of_oligo': 0
    }
    dna = Seq(target_dna)  # set biopython seq type
    result['GC_contents'] = '{:.2f} %'.format(GC(dna))
    result['Tm_value'] = MeltingTemp.Tm_Wallace(dna)
    result['Complement_seq'] = str(dna.complement())
    result['Reverse_complement_seq'] = str(dna.reverse_complement())
    result['Length_of_oligo'] = str(len(dna))

    return result


def Translate(target_dna):
    '''
    return should be dict type
    >>> gene.translate(table="Bacterial", to_stop=True)
    Seq('VKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDH...HHR')
    '''
    result = {
        'reverse_3': '',
        'reverse_2': '',
        'reverse_1': '',
        'forward_1': '',
        'forward_3': '',
        'forward_2': '',
    }
    dna_seq = Seq(target_dna)
    result['forward_1'] = str(dna_seq[0::].translate())
    result['forward_2'] = str(dna_seq[1::].translate())
    result['forward_3'] = str(dna_seq[2::].translate())
    result['reverse_1'] = str(dna_seq[:0:-1].translate())  # reverse frame
    result['reverse_2'] = str(dna_seq[:1:-1].translate())
    result['reverse_3'] = str(dna_seq[:2:-1].translate())
    return result
