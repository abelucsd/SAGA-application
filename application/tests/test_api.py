from application.models import Sample
from application import create_app

app = create_app()

def test_get_api_endpoint():
    sample_data = "#chrom1	start1	end1	chrom2	start2	end2	sample	score\n\
        chr19	36941198	36941199	chr19	37713243	37713244	S3	3.6227192282676697\n\
        chr19	33673128	33673129	chr19	36537999	36538000	S2	5.759157117921859\n\
        chr10	117087384	117087385	chr10	117536371	117536372	S1	7.984121944755316\n\
        chr12	117744401	117744402	chr20	11959745	11959746	S4	6.543943618424237\n"

    expected_response = [{ "sample": "S3", "chrom1": "chr19", "start1": 36941198, "end1": 36941199, "chrom2": "chr19", "start2": 37713243, "end2": 37713244, "score": 3.6227192282676697 }, 
        { "sample": "S2", "chrom1": "chr19", "start1": 33673128, "end1": 33673129, "chrom2": "chr19", "start2": 36537999, "end2": 36538000, "score": 5.759157117921859 }, 
        { "sample": "S1", "chrom1": "chr10", "start1": 117087384, "end1": 117087385, "chrom2": "chr10", "start2": 117536371, "end2": 117536372, "score": 7.984121944755316 }, 
        { "sample": "S4", "chrom1": "chr12", "start1": 117744401, "end1": 117744402, "chrom2": "chr20", "start2": 11959745, "end2": 11959746, "score": 6.543943618424237 }]
    
    with app.test_client() as c:
        c.post('/api', data = sample_data, content_type="text/xml")        
        response = c.get('/api')
        json_response = response.get_json()
        json_response == expected_response
        assert response.status_code == 200

def test_post_api_endpoint():
    sample_data = "#chrom1	start1	end1	chrom2	start2	end2	sample	score\n\
            chr19	36941198	36941199	chr19	37713243	37713244	S3	3.6227192282676697\n\
            chr19	33673128	33673129	chr19	36537999	36538000	S2	5.759157117921859\n\
            chr10	117087384	117087385	chr10	117536371	117536372	S1	7.984121944755316\n\
            chr12	117744401	117744402	chr20	11959745	11959746	S4	6.543943618424237\n"
    
    expected_response = [{ "sample": "S3", "chrom1": "chr19", "start1": 36941198, "end1": 36941199, "chrom2": "chr19", "start2": 37713243, "end2": 37713244, "score": 3.6227192282676697 }, 
        { "sample": "S2", "chrom1": "chr19", "start1": 33673128, "end1": 33673129, "chrom2": "chr19", "start2": 36537999, "end2": 36538000, "score": 5.759157117921859 }, 
        { "sample": "S1", "chrom1": "chr10", "start1": 117087384, "end1": 117087385, "chrom2": "chr10", "start2": 117536371, "end2": 117536372, "score": 7.984121944755316 }, 
        { "sample": "S4", "chrom1": "chr12", "start1": 117744401, "end1": 117744402, "chrom2": "chr20", "start2": 11959745, "end2": 11959746, "score": 6.543943618424237 }]
    
    sample_missing_col_data = "#chrom1	start1	end1	chrom2	start2	end2	sample\n\
            chr19	36941198	36941199	chr19	37713243	37713244	S3"
    
    expected_missing_col_response = {'msg': 'Error: missing column score.'}    

    with app.test_client() as c:
        response = c.post('/api', data = sample_data, content_type="text/xml")
        json_response = response.get_json()
        assert json_response == expected_response
        assert response.status_code == 201

        response = c.post('/api', data = sample_missing_col_data, content_type="text/xml")
        json_response = response.get_json()
        assert json_response == expected_missing_col_response
        assert response.status_code == 400