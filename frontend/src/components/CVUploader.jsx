import React, { useState } from 'react';
import axios from 'axios';
import LearningPathDisplay from './LearningPathDisplay';
import './CVUploader.css'; // Impor CSS baru
import { FaFileUpload, FaBullseye, FaFilePdf } from 'react-icons/fa'; // Ikon baru

const API_URL = import.meta.env.VITE_API_URL || 'http://188.166.197.4:8000';

function CVUploader() {
  const [file, setFile] = useState(null);
  const [jobTitle, setJobTitle] = useState('');
  const [learningPathData, setLearningPathData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleJobTitleChange = (event) => {
    setJobTitle(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file || !jobTitle) {
      setError('Silakan pilih file PDF dan isi target pekerjaan.');
      return;
    }
    setLoading(true);
    setError('');
    setLearningPathData(null);
    const formData = new FormData();
    formData.append('file', file);
    formData.append('job_title', jobTitle);
    try {
      const response = await axios.post(`${API_URL}/api/v1/cv/generate-path`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setLearningPathData(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Terjadi kesalahan saat memproses CV Anda.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="uploader-container">
        <div className="hero-section">
          <h1>Bangun Masa Depan Karir Anda</h1>
          <p>Unggah CV Anda, tentukan pekerjaan impian, dan biarkan AI menyusun jalur belajar paling optimal untuk Anda.</p>
        </div>

        <form onSubmit={handleSubmit} className="upload-form">
          <div className="form-step">
            <label htmlFor="file-upload">
              <FaFileUpload /> Langkah 1: Pilih CV Anda
            </label>
            <label htmlFor="file-upload" className="custom-file-input">
              {file ? (
                <>
                  <FaFilePdf size={30} color="var(--accent-hover)" />
                  <span className="file-name">{file.name}</span>
                </>
              ) : (
                <span>Klik atau seret file PDF ke sini</span>
              )}
            </label>
            <input id="file-upload" type="file" accept="application/pdf" onChange={handleFileChange} />
          </div>

          <div className="form-step">
            <label htmlFor="job-title">
              <FaBullseye /> Langkah 2: Tentukan Target Pekerjaan
            </label>
            <input
              id="job-title"
              type="text"
              value={jobTitle}
              onChange={handleJobTitleChange}
              placeholder="Contoh: Senior Backend Engineer (Go)"
            />
          </div>

          <button type="submit" disabled={loading} className="cta-button">
            {loading ? 'Menganalisis...' : 'Buat Jalur Belajar Saya'}
          </button>
        </form>

        {error && <p style={{ color: '#ff4d4d', marginTop: '1rem' }}>{error}</p>}
        {loading && (
          <div className="loading-spinner-container">
            <div className="spinner"></div>
            <p>AI sedang menyusun rencana... Ini mungkin memakan waktu sejenak.</p>
          </div>
        )}
      </div>

      {learningPathData && <LearningPathDisplay data={learningPathData} />}
    </>
  );
}

export default CVUploader;