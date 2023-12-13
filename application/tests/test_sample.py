from application.models import Sample
from application import create_app

app = create_app()        

def test_sample_creation():    
    sample = Sample()
    data = {
        'chrom1' : 'chr19',
        'start1' : 36941198,
        'end1' : 36941199,
        'chrom2' : 'chr19',
        'start2' : 37713243,
        'end2' : 37713244,
        'sample' : 'S3',
        'score' : 3.6227192282676697,
    }
        
    sample = Sample(
        chrom1 = 'chr19',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.chrom1 == data['chrom1']
    assert sample.start1 == data['start1']
    assert sample.end1 == data['end1']
    assert sample.chrom2 == data['chrom2']
    assert sample.start2 == data['start2']
    assert sample.end2 == data['end2']
    assert sample.sample == data['sample']
    assert sample.score == data['score']    

def test_sample_chrom1_field():   
       
    sample = Sample(
        chrom1 = 'chr19',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.chrom1 == 'chr19'
    assert sample.chrom1 != 'chr1'    

def test_sample_start1_field():
       
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.start1 == 36941198        
    assert sample.start1 != 123            

def test_sample_end1_field():
       
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.end1 == 36941199        
    assert sample.end1 != 123

def test_sample_chrom2_field():
           
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.chrom2 == 'chr19'
    assert sample.chrom1 != 'chr19'


def test_sample_start2_field():
           
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.start2 == 37713243        
    assert sample.start2 != 123


def test_sample_end2_field():
           
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.end1 == 37713244        
    assert sample.end1 != 123
            

def test_sample_end2_field():
           
    sample = Sample(
        chrom1 = 'chr1',
        start1 = 36941198,
        end1 = 36941199,
        chrom2 = 'chr19',
        start2 = 37713243,
        end2 = 37713244,
        sample = 'S3',
        score = 3.6227192282676697,
    )
    assert sample is not None
    assert sample.sample == 'S3'
    assert sample.sample != 'S1'
        

def test_sample_score_field():
       
    try:
        sample = Sample(
            chrom1 = 'chr1',
            start1 = 36941198,
            end1 = 36941199,
            chrom2 = 'chr19',
            start2 = 37713243,
            end2 = 37713244,
            sample = 'S3',
            score = 3.6227192282676697,
        )
        assert sample is not None
        assert sample.score != 3.6227192282676697    
        assert sample.score == 3.6227192282676697    

    # 3rd test should fail to output the correct validation message.
    except AssertionError as e:
        assert str(e) == 'assert 3.6227192282676697 != 3.6227192282676697\n +  where 3.6227192282676697 = <Sample S3>.score'


def test_sample_score_field_inrange():
       
    try:
        sample = Sample(
            chrom1 = 'chr1',
            start1 = 36941198,
            end1 = 36941199,
            chrom2 = 'chr19',
            start2 = 37713243,
            end2 = 37713244,
            sample = 'S3',
            score = 11,
        )
        assert sample is not None
        assert sample.score == 11
        assert sample.score == 3.6227192282676697
    
    # 3rd test should fail to output the correct validation message.
    except AssertionError as e:        
        assert str(e) == 'Score must be between 0 and 10: score 11 at <Sample S3>'